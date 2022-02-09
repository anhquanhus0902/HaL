const BubbleSort = require('./BubbleSort');
const SelectionSort = require('./SelectionSort');
const InsertionSort = require('./InsertionSort');
const QuickSort = require('./QuickSort');

const readline = require('readline').createInterface({
	input: process.stdin,
	output: process.stdout
});
// This array will be used for testing in case user doesn't input anything
const testArray = [
	-746, -142, -899, -91, 95, -264, 804, 627, 638, 846, 766, 13, -216, 837, -540, -555, -990, 175, -212, -292, -230, -941, -552, -724, -311, 933, 938, -130, 630, -482, 535, 955, -642, 583, -832, -466, 299, 661, -509, 640, -787, -439, 183, 965, 137, -183, -929, -183, 593, 41,
	708, 323, 978, -60, -572, -828, 229, -400, -853, 826, 339, 407, 453, 717, -183, -705, 155, -730, -827, -593, 915, 528, 158, -936, -37, -83, 246, 911, 749, -592, -168, -911, 885, 41, -996, 742, -901, -865, 653, 873, 360, 207, 914, 553, -721, -18, -681, 675, -432, 413
];
// Array used for testing
var arr;
// Variable that checks if all elements in the array are numeric
var areAllNum = true;

// Read input
readline.question('Enter the elements of the array on 1 line\n\
You can use testArray for testing by not entering input and just pressing Enter\n', elements => {
	// If user doesn't input anything, use testArray
	if (elements.trim().length === 0) {
		arr = testArray;
	}
	else {
		// Variable 'arr' now is an array of strings
		arr = elements.trim().split(/\s+/);
		// Traverse the array, checking if each element is a number and convert type to Float
		for (var i = 0; i < arr.length; ++i) {
			// If an element isn't a number, break the loop
			if (isNaN(parseFloat(arr[i]))) {
				console.log('Number only!');
				areAllNum = false;
				break;
			}
			arr[i] = parseFloat(arr[i]);
		}
	}
	if (areAllNum) {
		// Write the sorting function you want to use here
		// For example: BubbleSort.bubbleSort(arr);
		QuickSort.quickSort(arr);
		// Print the array after sorted
		console.log(arr);
	}
	readline.close();
});