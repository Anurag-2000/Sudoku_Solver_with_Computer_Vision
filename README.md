
## Real life Sudoku Solver 
### The main language used is python and the libereries used are OPEN CV and Tensorflow 2
Input IMG:
![1](https://user-images.githubusercontent.com/81687948/140780335-9dd87b50-b49d-415a-8d3d-75a0f07474b1.png)
  <ul>
    <li> the main couse of this project is to find a to sove a sudoku with just a clear photo of sudoku itself
      <ol>
          <li>there are 5 stages in this project
          <li>I will go over each one here
      </ol>
    <li>The 1st step is to create A number(digit) identifier
      <ol>
        <li>The <a href="https://github.com/Anurag-2000/digit_reco">digit classifier </a>is made Using Open CV with better image processing than usually done in MNSIT data base
        <li>I have also uploaded a repository on how i made my own model on detecting the correct digit
      </ol>
    <li>the 2nd step is to process the image
      <ol>
        <li>The Image goes under 4 processes till the point when logical code recives the array
        <li>we find the image Contours(boders)
          
![3](https://user-images.githubusercontent.com/81687948/140778571-1ceaafc6-0f74-454e-bb5d-d7d2bb54dba0.jpg)
        <li>we find the sudoku box
          
![4](https://user-images.githubusercontent.com/81687948/140778701-f29fae77-e3b6-4d43-89b9-27e3361c1852.jpg)
        <li>we crop it and wrap it into a plane full size image
          
![5](https://user-images.githubusercontent.com/81687948/140778826-208099bf-ddf5-4882-a108-f8c32d39fc9c.jpg)
        <li>finally we send crop image into 81 parts each containg 1 number of sudoku</li>
      </ol>
    <li>The 3rd step is to make the logical code for finding the solution of sudoku
      <ol>
        <li>Backtracking is used for the code 
        <li>this code is effitient than any brute force methord cus it will 9^81 guesses for it to work for a single cell
      </ol>
     <li>4th Sending the array to the code we wrote just above
        <ol>
          <li>this is send as a flat array and returned in the same manner with the answers
       </ol>
     <li>5th fianl step 
       <ol>
         <li>The Answers are printed on black screen dewraped
         <li> then it is merged on the orginal 
           
![2](https://user-images.githubusercontent.com/81687948/140781383-ea25d655-dcc9-4202-8efa-777516ee6400.png)
       </ol>
  </ul>
  
