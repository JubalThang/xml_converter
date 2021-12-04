const d = /(\d+)-(\d+)|(\d+)/g

function operation(b, c) {
    const converted = `
    <CHAPTER cnumber="${c}">
        ${b.replace(d, `</VERS><VERS vnumber="\$&">`)}</VERS>
    </CHAPTER>`


document.getElementById('ans').textContent = converted.replace('</VERS>', '')
// document.getElementById('ans').textContent = converted
}

const form = document.querySelector('form')
form.addEventListener('submit', e => {
    e.preventDefault()

    const bible = e.target.bible.value
    const cnumber = e.target.cnumber.value

    if(!cnumber){
        alert('Please provide a cnumber')
    } else if(!bible) {
        alert('Paste the bible')
    }
     else {
        operation('1'.concat('',bible),cnumber)
        e.target.reset()
    }
})