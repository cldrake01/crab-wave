use pyo3::pyfunction;

#[pyfunction]
fn add(a: i32, b: i32) -> i32 {
    a + b
}