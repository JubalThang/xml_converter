// find all verses eg. 1-5 or 1
// use i to ignore casesensative 
const d = /(\d+)-(\d+) |(\d+) /g

function operation(b) {
    const fix = b.replace(d, '</VERS><VERS vnumber="$&**"> ').replace(/late /ig, '').replaceAll(" **", '').concat('</VERS></CHAPTER>')
    const finalFix = fix.replace(`</VERS> </CHAPTER>`, '')
    document.getElementById('ans').textContent = finalFix
}

const form = document.querySelector('form')
form.addEventListener('submit', e => {
    e.preventDefault()

    const bible = e.target.bible.value
    operation(bible.replace(/LATE \d+/g, '</VERS> </CHAPTER> <CHAPTER cnumber="$&"> <VERS>').replaceAll('\n', ''))

})