use pyo3::{pymodule, pyfunction, PyResult, Python, wrap_pyfunction};
use pyo3::types::PyModule;

#[pyfunction]
fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {
    println!("Hello, world!");
}


#[pymodule]
fn crab_wave(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    Ok(())
}

