function operation(bible) {

    // const converted = .replace(/(\d+)-(\d+) |(\d+) /g, '</VERS><VERS vnumber="$&*"> ')
    const converted = bible.replace(/(\d+)-(\d+) |(\d+) /g, '</VERS><VERS vnumber="$&*"> ')

    const fixConverted = converted.replaceAll(/\nCH/g, '').replaceAll(' *', '').replaceAll('></VERS>', '>').concat('</VERS></CHAPTER>')
    const finalFix = fixConverted.replace(`</VERS> </CHAPTER>`, '')
    document.getElementById('ans').textContent = finalFix.replaceAll('\n', '')
    // document.getElementById('ans').textContent = bible
}

const form = document.querySelector('form')
form.addEventListener('submit', e => {
    e.preventDefault()

    const bible = e.target.bible.value

    if (!bible) {
        alert('Paste the bible')
    } else {
        const editedBible = bible.replace(/\d+\n/g, '</VERS> </CHAPTER> <CHAPTER cnumber="$&CH">1 ')

        operation(editedBible)
        e.target.reset()
    }
})