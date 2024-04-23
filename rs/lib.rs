// #[pymodule]
// fn crab_wave(_py: Python, m: &PyModule) -> PyResult<()> {
//     m.add_function(wrap_pyfunction!(haar_transform, m)?)?;
//     Ok(())
// }

extern crate nalgebra as na;

use na::DMatrix;

pub fn transform(signal: DMatrix<f64>, kernel: DMatrix<f64>) -> DMatrix<f64> {
    // Compute the dot product of the signal and the kernel
    // for each possible position of the kernel in the signal.
    let mut result = DMatrix::zeros(signal.nrows(), signal.ncols());
    
    result = signal.clone();
    
    for i in 0..signal.nrows() {
        for j in 0..signal.ncols() {
            let mut sum = 0.0;
            for k in 0..kernel.nrows() {
                for l in 0..kernel.ncols() {
                    if i + k < signal.nrows() && j + l < signal.ncols() {
                        sum += signal[(i + k, j + l)] * kernel[(k, l)];
                    }
                }
            }
            result[(i, j)] = sum;
        }
    }
    
    result
}

fn main() {
    println!("Hello, world!")
}
