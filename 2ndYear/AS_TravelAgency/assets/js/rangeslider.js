/*=============== RANGE SLIDER JS ===============*/
const rangeThumb = document.getElementById('range-thumb'),
      rangeNumber = document.getElementById('range-number'),
      rangeLine = document.getElementById('range-line'),
      rangeInput = document.getElementById('range-input')

const rangeInputSlider = () =>{

   // Insert the value of the input range
   rangeNumber.textContent = rangeInput.value

   // Calculate the position of the input thumb
   // rangeInput.value = 500, rangeInput.max = 1000, (500 / 1000 = 0.5)
   // rangeInput.offsetWidth = 248, rangeThumb.offsetWidth = 32, (248 - 32 = 216)
   const thumbPosition = (rangeInput.value / rangeInput.max),
         space = rangeInput.offsetWidth - rangeThumb.offsetWidth

   // We insert the position of the input thumb
   // thumbPosition = 0.5, space = 216 (0.5 * 216 = 108)
   rangeThumb.style.left = (thumbPosition * space) + 'px'

   // We insert the width to the slider with the value of the input value
   // rangeInput.value = 500, ancho = 50%
   rangeLine.style.width = rangeInput.value/10 + '%'

   // We call the range input
   rangeInput.addEventListener('input', rangeInputSlider)
}

rangeInputSlider()