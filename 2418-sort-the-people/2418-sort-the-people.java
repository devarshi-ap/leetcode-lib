class Solution {
    public static String[] sortPeople(String[] names, int[] heights) {
        Map<Integer, String> people = new HashMap<Integer, String>();
        List<Integer> sortedHeights = new ArrayList<>();
        String[] sortedNames = new String[names.length];

        for (int i=0; i<heights.length; i++)
            people.put(heights[i], names[i]);

        for (int h: heights) sortedHeights.add(h);
        Collections.sort(sortedHeights);
        Collections.reverse(sortedHeights);

        for (int i=0; i<sortedHeights.size(); i++)
            sortedNames[i] = people.get(sortedHeights.get(i));
        
        return sortedNames;
    }
}