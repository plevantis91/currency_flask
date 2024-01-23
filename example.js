const amount = 12345.67;


const formattedAmount1 = new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD',
}).format(amount);

console.log(formattedAmount1);

const formattedAmount2 = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'EUR',
  }).format(amount);
  
  console.log(formattedAmount2);

  const formattedAmount3 = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'INR',
  }).format(amount);
  
  console.log(formattedAmount3);
