package garden.plants.flowers;

import java.util.Objects;

import garden.plants.Plant;

/**
 * Represents a flower, which is a specific type of plant, that changes colors according
 * to the season, extending the generic Plant class.
 */
public class Flower extends Plant {
    private String winterColor;
    private String springColor;
    private String summerColor;
    private String autumnColor;

    // Flwoer constructor with specified colors for each season
    public Flower(String name, double waterConsumption, String winterColor, String springColor, String summerColor, String autumnColor) {
        super(name, waterConsumption);
        this.winterColor = winterColor;
        this.springColor = springColor;
        this.summerColor = summerColor;
        this.autumnColor = autumnColor;
    }

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
                return "*"; // For undefined season index
        }
    }
    
    /**
     * Checks if this Flower is equal to another Flower, by comparing both name and colors across all seasons
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Flower other = (Flower) obj;
        return Objects.equals(name, other.name) &&
               Objects.equals(winterColor, other.winterColor) &&
               Objects.equals(springColor, other.springColor) &&
               Objects.equals(summerColor, other.summerColor) &&
               Objects.equals(autumnColor, other.autumnColor);
    }

    // Returns hash value for the Flower based on name and seasonal colors
    @Override
    public int hashCode() {
        return Objects.hash(name, winterColor, springColor, summerColor, autumnColor);
    }

}
