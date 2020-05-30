  function popup_content(hideOrshow) {
    if (hideOrshow == 'hide') {
     document.getElementById('show_edit_bar').style.display = "none";
     }
    else {
    document.getElementById('show_edit_bar').removeAttribute('style');
    }
}

  function msh_popup(hideOrshow) {
    if (hideOrshow == 'hide') {
     document.getElementById('msh_show_edit_bar').style.display = "none";
     }
    else {
    document.getElementById('msh_show_edit_bar').removeAttribute('style');
    }
}