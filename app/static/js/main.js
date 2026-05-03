function toggleModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal.classList.contains('hidden')) {
        modal.classList.remove('hidden');
    } else {
        modal.classList.add('hidden');
    }
}

window.onclick = function(event) {
    const modals = document.getElementsByClassName('modal-overlay');
    for (let i = 0; i < modals.length; i++) {
        if (event.target == modals[i]) {
            modals[i].classList.add('hidden');
        }
    }
}
