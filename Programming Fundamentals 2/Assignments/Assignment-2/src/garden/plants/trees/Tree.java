package garden.plants.trees;

import java.util.Objects;

import garden.plants.Plant;

/**
 * Represents a tree, which is a specific type of plant that may produce fruit and 
 * changes colors according to the season. This class extends the generic Plant class.
 * 
 * Tree attributes, Name, water Consumption, and the seasonal colors as well as the Fruit produced by the Tree
 */
public class Tree extends Plant { 
    private String winterColor;
    private String springColor;
    private String summerColor;
    private String autumnColor;
    private String fruit;

    // Constructs a Tree instance with the previously named attributes 
    public Tree(String name, double waterConsumption, String winterColor, String springColor, String summerColor, String autumnColor, String fruit) {
        super(name, waterConsumption);
        this.winterColor = winterColor;
        this.springColor = springColor;
        this.summerColor = summerColor;
        this.autumnColor = autumnColor;
        this.fruit = fruit;
    }
    
    // Fruit produced by the Tree
    public String getFruit() {
        return fruit;
    }

    // Returns color of the Tree based on the given Seasons
    @Override
    public String colour(int season) {
        switch (season) {
            case 0:
                return winterColor;
            case 1:
                return springColor;
            case 2:
                return summerColor;
            case 3:
                return autumnColor;
            default:
                return "*"; // Returns * for unspecified season
        }
    }
    
    // Checks if Tree is equal to another Tree based on name, seasonal colors and fruit produced
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Tree other = (Tree) obj;
        return Objects.equals(name, other.name) &&
               Objects.equals(winterColor, other.winterColor) &&
               Objects.equals(springColor, other.springColor) &&
               Objects.equals(summerColor, other.summerColor) &&
               Objects.equals(autumnColor, other.autumnColor) &&
               Objects.equals(fruit, other.fruit);
    }

    // Returns hash value of the tree based on name, seaonsal colors and fruit produced 
    @Override
    public int hashCode() {
        return Objects.hash(name, winterColor, springColor, summerColor, autumnColor, fruit);
    }

}
