const data = [-0.00193587,  0.06788393,  0.7757792,  -1.3098741 ]

const etiquetasX = [];
let polinomio = "";

for (let i = 1; i <= data.length; i++) {
    etiquetasX.push(`x^${data.length-i}`);
    polinomio += `${data[i-1]}x^${data.length-i} `
}
console.log(polinomio)