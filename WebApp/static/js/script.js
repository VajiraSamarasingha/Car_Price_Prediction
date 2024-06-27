
const currentYear = new Date().getFullYear();
const startYear = 2000;
const endYear = currentYear + 5; 
const yearSelect = document.getElementById('year');


for (let year = startYear; year <= endYear; year++) {
    const option = document.createElement('option');
    option.value = year;
    option.text = year;
    yearSelect.appendChild(option);
}