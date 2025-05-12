function deleteNote(noteId)
{
    fetch('/deleteNote', {
        method: 'POST',
        headers:
        {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({noteId:noteId}),
}).then((_res) => 
{
    window.location.href='/';
});

}