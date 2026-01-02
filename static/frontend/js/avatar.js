function avatarSpeaking(speaking) {
    const avatarImg = document.getElementById("avatar");
    if (speaking) {
        avatarImg.src = "/static/frontend/assets/avatars/dt5.jpg";
        avatarImg.classList.add("speaking");
    } else {
        avatarImg.src = "/static/frontend/assets/avatars/dt1.jpg";
        avatarImg.classList.remove("speaking");
    }
}
