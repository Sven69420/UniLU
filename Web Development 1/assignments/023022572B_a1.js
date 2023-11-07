let countZeros = 0;
let countObstacles = 0;
//variables that store the zero count (named "countZero") and the obstacles count (everything bigger than zero, named "countObstacles")

/*
M = [
    [ 1, 1, 2, 2, 1, 1, 1, 3 ],
    [ 1, 0, 1, 0, 0, 0, 0, 3 ],
    [ 1, 0, 2, 1, 3, 3, 0, 1 ],
    [ 3, 0, 0, 0, 0, 1, 1, 1 ],
    [ 2, 0, 4, 1, 1, 0, 4, 1 ],
    [ 1, 0, 0, 0, 3, 0, 0, 1 ],
    [ 1, 0, 0, 2, 3, 0, 4, 4 ]
   ];
*/

//The matrix(M) used as example, also used to test this code
//made into a comment since the goal was to not declare a matrix when submitting the code

for (let i = 0; i < M.length; i++) { //sets up a loop that iterates through the rows of the matrix(M), starting with row 0
    for (let j = 0; j < M[i].length; j++){ //sets up a loot that iterates thorugh the all columns within the current row, starting also with 0
        if (M[i][j] === 0){
            countZeros++; //determines if M_ij is 0 and increases countZero accordingly, to count the number of zeros in each row and column
        } else if (M[i][j] >= 2){
            M[i][j] *=2; //doubles every number greater than or equal to 2 (by multiplying it by 2 and updating the existing variable (short verison of M[i][j] = M[i][j] * 2))
        }
        if (M[i][j] > 0){
            countObstacles++; //determines if M_ij is bigger than 0 and increases countObstacles accordingly, to count the number of every number greater than 0 in each row and column
        }
    }
}

console.log("Number of entries that are 0: " + countZeros);
console.log("Number of entries that are greater than 0: " + countObstacles);
console.log("Matrix after doubling values greater than or equal to 2: ");
console.log(M);
//outputs the various tasks given in the homework, i.e. the zero count, the obstacles count, the matrix with every number bigger than 2 doubled, in this sequence, so the zero count first, etc. 