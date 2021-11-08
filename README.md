## Real life Sudoku Solver 
<h3> The main language used is python and the libereries used are OPEN CV and Tensorflow 2.
  <ul>
    <li> the main couse of this project is to find a to sove a sudoku with just a clear photo of sudoku itself
      <ol>
          <li>there are n stages in this project
          <li>I will go over each one here
      </ol>
    <li>The 1st step is to create A number(digit) identifier
      <ol>
        <li>The digit classifier is made Using Open CV with better image processing than usually done in MNSIT data base
        <li>I have also uploaded a repository on how i made my own model on detecting the correct digit
      </ol>
    <li>the 2nd step is to process the image
      <ol>
        <li>The Image goes under 4 processes till the point when logical code recives the array
        <li>we find the image Contours(boders)
        <li>we find the sudoku box
        <li>we crop it and wrap it into a plane full size image
        <li>finally we send crop image into 81 parts each containg 1 number of sudoku
      </ol>
    <li>The next step is to make the logical code for finding the solution of sudoku
      <ol>
        <li>Backtracking is used for the code 
        <li>this code is effitient than any brute force methord cus it will 9^81 guesses for it to work for a single cell
      </ol>

     <li>Sending the array to the code we wrote just above
        <ol>
          <li>this is send as a flat array and returned in the same manner with the answers
       </ol>
     <li>fianl step 
       <ol>
         <li>The Answers are printed on black screen dewraped
         <li> then it is merged on the orginal 
       </ol>
  </ul>
