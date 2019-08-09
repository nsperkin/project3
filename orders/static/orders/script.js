document.addEventListener('DOMContentLoaded', () => {
	
	/*************************Pizza***************************/
	var limit = 0;
	document.querySelectorAll('.sel1').forEach(function(row) {
		row.onclick = () => {
			const style = row.cells[0].innerHTML;
			const num_toppings = row.cells[1].innerHTML;
			limit = row.cells[1].innerHTML;
			const size = row.cells[2].innerHTML;
			const price = row.cells[3].innerHTML;
			document.querySelector('.toast').style.visibility = "visible";
			document.querySelector('.price').innerHTML = price;
			document.querySelector('#extras').style.display = "none";
			document.querySelector('#new').setAttribute("value", "pizza")
			document.querySelector('#pk').setAttribute("value", row.cells[4].innerHTML);

			if (num_toppings == 0) {
				document.querySelector('.item').innerHTML = `${size} ${style} Cheese Pizza`;
				document.querySelector('#toppings').style.display = "none";
			}
			else {
				document.querySelector('.item').innerHTML = `${size} ${style} ${num_toppings} Topping Pizza`;
				document.querySelector('#toppings').style.display = "block";
			}
		};
	});

	// set max number of toppings
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


	/*************************Sub***************************/
	document.querySelectorAll('.sel2').forEach(function(row) {
		row.onclick = () => {
			const style = row.cells[0].innerHTML;
			const size = row.cells[1].innerHTML;
			const price = row.cells[2].innerHTML;
			document.querySelector('.toast').style.visibility = "visible";
			document.querySelector('.price').innerHTML = price;
			document.querySelector('.item').innerHTML = `${size} ${style} Sub`;
			document.querySelector('#toppings').style.display = "none";
			document.querySelector('#new').setAttribute("value", "sub");
			document.querySelector('#pk').setAttribute("value", row.cells[3].innerHTML);



			document.querySelector('#extras').style.display = "block";
		};
	});

	// add %.50 for extras
	document.querySelectorAll('.xtra').forEach(function(extra) {
		extra.onclick = () => {
			var price = document.querySelector('.price')
			if(extra.checked) {
				price.innerHTML = (Number(price.innerHTML) + .5).toFixed(2);
			}
			else {
				price.innerHTML = (Number(price.innerHTML) - .5).toFixed(2);
			}
		};
	});

	/*************************Pasta***************************/
	document.querySelectorAll('.sel3').forEach(function(row) {
		row.onclick = () => {
			const style = row.cells[0].innerHTML;
			const price = row.cells[1].innerHTML;
			document.querySelector('.toast').style.visibility = "visible";
			document.querySelector('.price').innerHTML = price;
			document.querySelector('.item').innerHTML = `${style} Pasta`;
			document.querySelector('#toppings').style.display = "none";
			document.querySelector('#extras').style.display = "none";
			document.querySelector('#new').setAttribute("value", "pasta");
			document.querySelector('#pk').setAttribute("value", row.cells[2].innerHTML);

		};
	});

	/*************************Salad***************************/
	document.querySelectorAll('.sel4').forEach(function(row) {
		row.onclick = () => {
			const style = row.cells[0].innerHTML;
			const price = row.cells[1].innerHTML;
			document.querySelector('.toast').style.visibility = "visible";
			document.querySelector('.price').innerHTML = price;
			document.querySelector('.item').innerHTML = `${style}`;
			document.querySelector('#toppings').style.display = "none";
			document.querySelector('#extras').style.display = "none";
			document.querySelector('#new').setAttribute("value", "salad");
			document.querySelector('#pk').setAttribute("value", row.cells[2].innerHTML);

		};
	});

	/*************************Dinner Platter***************************/
	document.querySelectorAll('.sel5').forEach(function(row) {
		row.onclick = () => {
			const style = row.cells[0].innerHTML;
			const size = row.cells[1].innerHTML;
			const price = row.cells[2].innerHTML;
			document.querySelector('.toast').style.visibility = "visible";
			document.querySelector('.price').innerHTML = price;
			document.querySelector('.item').innerHTML = `${size} ${style} Dinner Platter`;
			document.querySelector('#toppings').style.display = "none";
			document.querySelector('#extras').style.display = "none";
			document.querySelector('#new').setAttribute("value", "dinner_platter");
			document.querySelector('#pk').setAttribute("value", row.cells[3].innerHTML);
		};
	});

	document.querySelector('#submit').onclick = () => {
		var price = document.querySelector('.price').innerHTML;
		document.querySelector('#price').setAttribute("value", price);
	};


	// Close Button
	document.querySelector('.close').onclick = () => {
		document.querySelector('.toast').style.visibility = "hidden";
	};
});


