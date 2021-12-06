

function operation(b) {
    // const converted = `
    // <CHAPTER cnumber="${c}">
    //     ${b.replace(d, `</VERS><VERS vnumber="\$&">`)}</VERS>
    // </CHAPTER>`

    const converted = b.replace(/Late \d+/g , '</CHAPTER> <CHAPTER cnumber="$&**">').replace(/(\d+)-(\d+) |(\d+) /g, '</VERS><VERS vnumber="$&">')
    
    document.getElementById('ans').textContent = converted
}

const form = document.querySelector('form')
form.addEventListener('submit', e => {
    e.preventDefault()

    const bible = e.target.bible.value

    if (!bible) {
        alert('Paste the bible')
    } else {
        operation(bible)
        e.target.reset()
    }
})