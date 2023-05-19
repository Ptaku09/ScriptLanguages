// Onclick of the button
document.querySelector("button").onclick = () => {
// Call python's random_python function
  eel.random_python()((number) => {
    // Update the div with a random number returned by python
    document.querySelector(".random_number").innerHTML = number;
  })
}
