let menu_opened = false;

function MenuListManager() {
	const list = document.getElementById("menu_list");

	menu_opened = !menu_opened;

	if (menu_opened) {
		list.style.transform = "translateX(0px)";
	} else {
		list.style.transform = "translateX(-100%)";
	}
}
