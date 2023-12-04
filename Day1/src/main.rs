// use std::env;
use std::fs;


fn main() {
    let content = fs::read_to_string("./text.txt")
                            .expect("File should have been read");

    for line in content.lines() {
        let mut array = Vec::new();
        
        for letter in line.chars(){
            if !letter.is_alphabetic(){
                array.push(letter);
            }
        }
        
                
        println!("{:?}", array)
    }
}
