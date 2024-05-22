package Assginments;
import java.util.Random;
import java.util.Scanner;

public class LabyrinthGame {
    // Class constants for labyrinth settings
    private static final int ROWS = 20;
    private static final int COLS = 40;
    private static final char WALL = '#';
    private static final char EMPTY = ' ';
    private static final char PLAYER = 'P';
    private static final char EXIT = 'E';
    // Labyrinth represented as a 2D array
    private char[][] labyrinth = new char[ROWS][COLS];
    // Player's initial position
    private int playerRow = ROWS - 1;
    private int playerCol = 0;

    public LabyrinthGame() {
        generateLabyrinth();
        placePlayerAndExit();
    }

    // Generate the labyrinth with walls and empty spaces
    private void generateLabyrinth() {
        Random random = new Random();
        for (int i = 0; i < ROWS; i++) { // loop for the rows
            for (int j = 0; j < COLS; j++) { // loop for the columns
                // Initially set all positions to empty
                labyrinth[i][j] = EMPTY;
            }
            // Add a random wall to each row except the first and last
            if (i > 0 && i < ROWS - 1) {
                int wallPos = random.nextInt(COLS);
                labyrinth[i][wallPos] = WALL;
            }
        }
    }

    // Place the player and the exit in the labyrinth
    private void placePlayerAndExit() {
        labyrinth[playerRow][playerCol] = PLAYER; // Player starting position
        labyrinth[0][COLS - 1] = EXIT; // Exit position
    }

    // Display the current state of the labyrinth
    public void displayLabyrinth() {
        // Print the top border
        for (int i = 0; i < COLS + 2; i++) { // +2 accounts for the side borders
            System.out.print("-");
        }
        System.out.println();

        // Existing loop for the labyrinth rows, with side borders
        for (int i = 0; i < ROWS; i++) {
            System.out.print("|"); // Print left side border before each row
            for (int j = 0; j < COLS; j++) {
                System.out.print(labyrinth[i][j]); // Print the row contents
            }
            System.out.println("|"); // Print right side border after each row
        }

        // Print the bottom border after all rows have been printed
        for (int i = 0; i < COLS + 2; i++) {
            System.out.print("-");
        }
        System.out.println();
    }


    // Move the player based on input direction
    public void movePlayer(char direction) {
        // Calculate the new potential position based on the direction
        int newRow = playerRow;
        int newCol = playerCol;
        
        switch (direction) {
            case 'w': newRow--; break; // Up
            case 's': newRow++; break; // Down
            case 'a': newCol--; break; // Left
            case 'd': newCol++; break; // Right
        }

        // Check if the new position is within bounds and not a wall
        if (newRow >= 0 && newRow < ROWS && newCol >= 0 && newCol < COLS && labyrinth[newRow][newCol] != WALL) {
            // Update the labyrinth to reflect the player's movement
            labyrinth[playerRow][playerCol] = EMPTY;
            playerRow = newRow; // Player row
            playerCol = newCol; // Player column
            // Check if the player has reached the exit
            if (labyrinth[playerRow][playerCol] == EXIT) {
                System.out.println("Congratulations! You've reached the exit!"); // Congratulatory message
                System.exit(0); // End the game
            }
            labyrinth[playerRow][playerCol] = PLAYER;
        } else {
            System.out.println("Movement not possible."); // Invalid move
        }
    }

    public static void main(String[] args) {
        LabyrinthGame game = new LabyrinthGame();
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            game.displayLabyrinth(); // Show the labyrinth
            System.out.println("Use WASD to move. Enter your move: "); // Get player input
            String input = scanner.nextLine();
            if (input.length() > 0) { 
                char move = input.toLowerCase().charAt(0);
                game.movePlayer(move); // Process the player's move
            }
        }
    }
}
