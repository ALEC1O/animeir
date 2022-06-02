window.onresize = () => {
	OnResizePoster();
};

OnResizePoster();

function OnResizePoster() {
	try {
		const all = document.querySelectorAll(".image--poster");

		all.forEach((image) => {
			const oldHeight = image.clientHeight;
			const newHeight = image.clientWidth * 1.5;

			const target = image.querySelector(".poster_1");

			if (target) {
				target.style.minHeight = `${newHeight}px`;
				target.style.maxHeight = `${newHeight}px`;
			}
		});
	} catch {}

	try {
		const all = document.querySelectorAll(".image_background");

		all.forEach((image) => {
			const oldHeight = image.clientHeight;
			const newHeight = image.clientWidth * 0.57;

			const target = image.querySelector(".poster_1");

			if (target) {
				target.style.minHeight = `${newHeight}px`;
				target.style.maxHeight = `${newHeight}px`;
			}
		});
	} catch {}

	console.log("OnResize Poster");
}
