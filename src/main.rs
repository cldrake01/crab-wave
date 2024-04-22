

// #[pymodule]
// fn crab_wave(_py: Python, m: &PyModule) -> PyResult<()> {
//     m.add_function(wrap_pyfunction!(haar_transform, m)?)?;
//     Ok(())
// }

fn haar_transform(signal: &[f64]) -> Vec<f64> {
    let mut output = vec![0.0; signal.len()];

    let mut approximation = vec![0.0; signal.len() / 2];
    let mut detail = vec![0.0; signal.len() / 2];

    for i in 0..signal.len() / 2 {
        approximation[i] = (signal[2 * i] + signal[2 * i + 1]) / 2.0;
        detail[i] = (signal[2 * i] - signal[2 * i + 1]) / 2.0;
    }

    output[..signal.len() / 2].copy_from_slice(&approximation);
    output[signal.len() / 2..].copy_from_slice(&detail);

    output
}

fn main() {
    let signal = vec![1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0];
    let transformed = haar_transform(&signal);
    println!("Transformed: {:?}", transformed);
}



