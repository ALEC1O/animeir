window.onresize = () => {
	ResizeAnimePoster();
};

ResizeAnimePoster();

function ResizeAnimePoster() {
	try {
		const all = document.querySelectorAll(".poster_anime");

		all.forEach((e) => {
			e.style.height = `${e.clientWidth * 1.5}px`;
		});
	} catch {}

	try {
		const all = document.querySelectorAll(".poster_episode");

		all.forEach((e) => {
			e.style.height = `${e.clientWidth * 1.5}px`;
		});
	} catch {}

	console.log("onresize");
}
