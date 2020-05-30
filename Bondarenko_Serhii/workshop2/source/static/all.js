  function ppup_content(hideOrshow) {
    if (hideOrshow == 'hide') {
     document.getElementById('show_add_u_bar').style.display = "none";
     }
    else {
    document.getElementById('show_add_u_bar').removeAttribute('style');
    }
}

  function h_popup(hideOrshow) {
    if (hideOrshow == 'hide') {
     document.getElementById('show_add_m_bar').style.display = "none";
     }
    else {
    document.getElementById('show_add_m_bar').removeAttribute('style');
    }
}