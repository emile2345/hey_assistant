const callBtn = document.getElementById("callBtn");
const hangupBtn = document.getElementById("hangupBtn");
const acceptBtn = document.getElementById("acceptBtn");
const avatar = document.getElementById("avatar");
const ringTone = document.getElementById("ringTone");

let audioPlayer = null;
let calling = false;

// Fonction avatar
function avatarSpeaking(speaking) {
    avatar.src = speaking ? "/static/frontend/assets/avatars/dt5.jpg"
        : "/static/frontend/assets/avatars/dt1.jpg";
}

// ----------- Appeler ----------- //
callBtn.onclick = async () => {
    try {
        const res = await fetch("/call/start", { method: "POST" });
        if (!res.ok) { alert("Erreur démarrage appel"); return; }

        calling = true;
        ringTone.play();   // jouer sonnerie
        avatarSpeaking(false);

    } catch (err) {
        console.error(err);
        alert("Erreur réseau");
    }
};

// ----------- Accepter ----------- //
acceptBtn.onclick = async () => {
    if (!calling) return;

    ringTone.pause();
    ringTone.currentTime = 0;

    // Avatar parle
    avatarSpeaking(true);

    // Jouer voix HEY Assistant
    try {
        const voiceRes = await fetch("/voice/speak", { method: "POST" });
        if (!voiceRes.ok) { alert("Erreur voix"); return; }

        const audioBlob = await voiceRes.blob();
        const audioUrl = URL.createObjectURL(audioBlob);
        audioPlayer = new Audio(audioUrl);
        audioPlayer.play();

        audioPlayer.onended = () => {
            avatarSpeaking(false);
            calling = false;
        };
    } catch (err) {
        console.error(err);
        avatarSpeaking(false);
        calling = false;
    }
};

// ----------- Raccrocher ----------- //
hangupBtn.onclick = async () => {
    try {
        await fetch("/call/stop", { method: "POST" });
        calling = false;

        // Stop sonnerie
        ringTone.pause();
        ringTone.currentTime = 0;

        // Stop voix
        if (audioPlayer) {
            audioPlayer.pause();
            audioPlayer.currentTime = 0;
            audioPlayer = null;
        }

        avatarSpeaking(false);

    } catch (err) {
        console.error(err);
    }
};
