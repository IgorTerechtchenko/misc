package hangman;

import java.util.Random;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Singleton class for choosing random word from file.
 */
public class WordChooser {
	
	private WordChooser() {}
	
	public static String getRandomWord(String filename) throws IOException {
		ArrayList<String> wordsList = new ArrayList<>();
		FileInputStream stream = new FileInputStream(filename);
		Scanner scan = new Scanner(stream);
		while (scan.hasNext()) {
			wordsList.add(scan.next());
		}
		scan.close();
		stream.close();
		Random rand = new Random();
		return wordsList.get(rand.nextInt(wordsList.size()));
	}
}