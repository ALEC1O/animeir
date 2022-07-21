let background_size = 0;
let poster_size = 0;

window.onresize = () => {
	OnResizePoster();
};

OnResizePoster();

function PosterButton(type, dir, self) {
	let s = document.querySelector("aa");
	if (self) s = self;
	const poster = s.parentElement.parentElement.querySelector(".poster");

	if (type && dir && self) {
		if (type === "background") {
			poster.scrollLeft += background_size * dir;
		} else if (type == "poster") {
			poster.scrollLeft += poster_size * dir;
		}
	}
}

function OnResizePoster() {
	try {
		const all = document.querySelectorAll(".image_poster");

		all.forEach((image) => {
			const oldHeight = image.clientHeight;
			const newHeight = image.clientWidth * 1.5;
			poster_size = image.clientWidth;

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
			background_size = image.clientWidth;

			const target = image.querySelector(".poster_1");

			if (target) {
				target.style.minHeight = `${newHeight}px`;
				target.style.maxHeight = `${newHeight}px`;
			}
		});
	} catch {}

	try {
		const all = document.querySelectorAll(".poster_container");

		all.forEach((poster_container) => {
			const buttons = poster_container.querySelector(".poster_buttons");
			const poster = poster_container.querySelector(".poster");
			let removeHeight = 0;

			if (poster) {
				const poster_2 = poster.querySelector(".poster_2");
				removeHeight = poster_2.clientHeight;
			}

			if (buttons) {
				const calc = (poster.clientHeight - removeHeight) / 2;
				buttons.style.marginTop = `${calc}px`;
				buttons.style.height = `${0}px`;
				buttons.style.width = `${poster_container.clientWidth}px`;
			}
		});
	} catch {}

	console.log("OnResizePoster...");
}
