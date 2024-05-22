package garden;

import garden.Ornament;
import garden.plants.Plant;

/**
 * Represents a garden which is a grid of ornaments, plants and tiles
 */
public class Garden {
    private Ornament[][] grid; // Grid representing a garden, where each cell can contain an ornament

    // Creates a garden instance with specific rows and column numbers
    public Garden(int rows, int columns) {
        grid = new Ornament[rows][columns];
    }

    // Adds an ornament to the specified postion in the garden grid
    public boolean add(int rowPosition, int columnPosition, Ornament ornament) {
        if (grid[rowPosition][columnPosition] == null) {
            grid[rowPosition][columnPosition] = ornament;
            return true;
        }
        return false;
    }

    // Removes ornament from specified position in the garden
    public void remove(int rowPosition, int columnPosition) {
        grid[rowPosition][columnPosition] = null;
    }

    // Counts the total number of ornaments within the garden
    public int count() {
        int count = 0;
        for (Ornament[] row : grid) {
            for (Ornament o : row) {
                if (o != null) count++;
            }
        }
        return count;
    }

    // Displays the names of the ornaments within the garden
    public void displayNames() {
        for (Ornament[] row : grid) {
        	for (Ornament ornament : row) {
        		if (ornament != null) {
        			System.out.print(String.format("%12s", ornament.getName())); 
        		} else {
        			System.out.print(String.format("%12s", "*")); 
        		}
        	}
        	System.out.println(); // Move to the next line after printing each row
        }
    }

    // Displays the colors of the ornamnets within the garden for the specific seasons
    public void displayColours(int season) {
        if (season < 0 || season > 3) return; // Early exit if the season is invalid

        for (Ornament[] row : grid) {
            for (Ornament ornament : row) {
                if (ornament != null) {
                    String color = ornament.colour(season); // Get the color for the season
                    if ("None".equals(color) || color == null) { // Check if the color is "None" or null
                        System.out.print(String.format("%12s", "*")); // Print "*" if color is "None"
                    } else {
                        System.out.print(String.format("%12s", color)); // Otherwise, print the actual color
                    }
                } else {
                    System.out.print(String.format("%12s", "*")); // Display "*" if the ornament is null
                }
            }
            System.out.println(); // Move to the next line after printing each row
        }
    }



    // Calculates total water consumption of the garden's plants
    public double consumedWater(int days) {
        double totalWater = 0;
        for (Ornament[] row : grid) {
            for (Ornament o : row) {
                if (o instanceof Plant) {
                    totalWater += ((Plant) o).consumedWater(days);
                }
            }
        }
        return totalWater;
    }

    // Counts the number of occurences of specific ornaments within the garden
    public int count(Ornament targetOrnament) {
    	 int count = 0;
    	    for (Ornament[] row : grid) {
    	        for (Ornament ornament : row) {
    	            if (ornament != null && ornament.equals(targetOrnament)) {
    	                count++;
    	            }
    	        }
    	    }
    	    return count;
    }
}
