function operation(bible) {

    const converted = bible.replace(/(\d+)-(\d+) |(\d+) /g, '</VERS><VERS vnumber="$&*"> ')

    const fixConverted = converted.replaceAll(/\nCH/g, '').replaceAll(' *', '').replaceAll('></VERS>', '>').concat('</VERS></CHAPTER>')
    const finalFix = fixConverted.replace(`</CHAPTER>`, '')
    document.getElementById('ans').textContent = finalFix.replace(`</VERS>`, '').replaceAll(/\n/g,'')
}

const form = document.querySelector('form')
form.addEventListener('submit', e => {
    e.preventDefault()

    const bible = e.target.bible.value

    if (!bible) {
        alert('Paste the bible')
    } else {
        // const editedBible = bible.replace(/\d+\n/, '</VERS> </CHAPTER> <CHAPTER cnumber="$&**">').replace(/\d+/g, '$& ')
        const editedBible = bible.replace(/\d+\n/g, '</VERS> </CHAPTER> <CHAPTER cnumber="$&CH"> ')

        operation(editedBible)
        e.target.reset()
    }
})