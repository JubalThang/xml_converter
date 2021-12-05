const d = /(\d+)-(\d+)|(\d+)/g

function operation(b, c) {
    const converted = `
    <CHAPTER cnumber="${c}">
        ${b.replace(d, `</VERS><VERS vnumber="\$&">`)}</VERS>
    </CHAPTER>`
    document.getElementById('ans').textContent = converted.replace('</VERS>', '')
    // console.log(b, c)
}

const form = document.querySelector('form')
form.addEventListener('submit', e => {
    e.preventDefault()

    const bible = e.target.bible.value

    if (!bible) {
        alert('Paste the bible')
    } else {
        const cnumber = bible.match(/\d+/)
        const newB = bible.replace(/\d+/, '1')
            // operation('1'.concat('', bible), cnumber[0])
        operation(newB, cnumber[0])
        e.target.reset()
    }
})