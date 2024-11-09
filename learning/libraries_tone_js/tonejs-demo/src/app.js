const synth = new Tone.Synth().toDestination();

document.getElementById('playButton').addEventListener('click', () => {
    synth.triggerAttackRelease('C4', '8n');
});

document.getElementById('stopButton').addEventListener('click', () => {
    synth.triggerRelease();
});