use pyo3::types::PyModule;
use pyo3::{pyfunction, pymodule, wrap_pyfunction, PyResult, Python};
use std::iter;

#[pyfunction]
fn dot(a: Vec<f64>, b: Vec<f64>) -> PyResult<f64> {
    let zipped = iter::zip(a.iter(), b.iter());
    Ok(zipped.map(|(x, y)| x * y).sum::<f64>().into())
}

#[pymodule]
fn cw(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(dot, m)?)?;
    Ok(())
}
