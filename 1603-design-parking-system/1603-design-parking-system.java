class ParkingSystem {

    int[] parking = new int[3];

    public ParkingSystem(int big, int medium, int small) {
        this.parking[0] = big;
        this.parking[1] = medium;
        this.parking[2] = small;
    }
    
    public boolean addCar(int carType) {
        boolean hasSpace = (this.parking[carType-1] >= 1) ? true : false;
        if (hasSpace) {
            this.parking[carType-1] -= 1;
            return true;
        } else {
            return false;
        }
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */