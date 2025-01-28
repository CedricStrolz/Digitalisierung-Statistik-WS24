fn main() {
    println!("Hello World!");

    let x1 = 2;
    let y1 = 7;
    let x2 = -3;
    let y2 = -8;

    let k = (y2 - y1) as f64 / (x2 - x1) as f64;
    let d = y1 as f64 - k * x1 as f64;

    println!("Steigung (k): {:.2}", k);
    println!("Ordinatenabschnitt (d): {:.2}", d);
    println!("f(x) = {:.2}*x + {:.2}", k, d);
  
    let string = "Digitalisierung und Statistik";
    let ausgabe: String = string.chars().skip(2).step_by(3).collect();
    println!("{}", ausgabe);

    let string2 = "vitaler nebel mit sinn ist im leben relativ";
    let ausgabe2: String = string2.chars().rev().collect();
    println!("{}", ausgabe2);

    let mut string3 = String::from("Heute arbeitet er am Comuter etwas länger");
    string3 = string3.replace("er", "sie");
    println!("{}", string3);

    let jahre = [1984, 2004, 2024];
    for &j in &jahre {
        let k = j / 100;
        let m = 15 + (3 * k + 3) / 4 - (8 * k + 13) / 25;
        let s = 2 - (3 * k + 3) / 4;
        let a = j % 19;
        let d = (19 * a + m) % 30;
        let r = (d + a / 11) / 29;
        let og = 21 + d - r;
        let sz = 7 - (j + j / 4 + s) % 7;
        let oe = 7 - (og - sz) % 7;
        let os = og + oe;

        let (tag, monat) = if os > 31 {
            (os - 31, "April")
        } else {
            (os, "Maerz")
        };

        println!("{} {}", tag, monat);
    }
}
