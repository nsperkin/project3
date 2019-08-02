document.addEventListener('DOMContentLoaded', () => {
	var limit = 0;
	document.querySelectorAll('.select').forEach(function(row) {
		row.onclick = () => {
			const style = row.cells[0].innerHTML;
			const num_toppings = row.cells[1].innerHTML;
			limit = row.cells[1].innerHTML;
			const size = row.cells[2].innerHTML;
			const price = row.cells[3].innerHTML;
			document.querySelector('.toast').style.visibility = "visible";
			document.querySelector('.price').innerHTML = price;
			if (num_toppings == 0) {
				document.querySelector('.item').innerHTML = `${size} ${style} Cheese pizza`;
				document.querySelector('#item').style.display = "none";
			}
			else {
				document.querySelector('.item').innerHTML = `${size} ${style} ${num_toppings} Topping Pizza`;
				document.querySelector('#item').style.display = "block";
			}
		};
	});

	document.querySelector('.close').onclick = () => {
		document.querySelector('.toast').style.visibility = "hidden";
	};

	var counter = 0;
	document.querySelectorAll('.top').forEach(function(topping) {
		topping.onclick = () => {
			var checked = document.querySelectorAll('input[type="checkbox"]:checked').length;
			if(topping.checked && checked>limit){
				alert(`Please select a maximum of ${limit} toppings!`);
				topping.checked = false;
			}
		};
	});
});