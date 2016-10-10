package hangman;

import java.io.IOException;
import java.util.Scanner;

public class Hangman {
	
	private static Game game;
	private static HangmanOutput output;
	private static final int HANGMAN_PARTS = 9;
	private static final char DELIMITER = '#';

	public static void main(String[] args) {
		try {
			game = new Game(args[0], HANGMAN_PARTS);
			output = new HangmanOutput(System.out);
			char guess;
			Scanner s = new Scanner(System.in);
			while(true) {
				output.println(game.getWord(DELIMITER));
				output.println(game.getTriedLetters());
				output.println("Make your guess:");
				try {
					guess = s.nextLine().charAt(0);
				} catch ( java.lang.StringIndexOutOfBoundsException e) {
					output.println("Enter letter to proceed:");
					continue;
				}
				game.tryLetter(guess);
				
				output.println(game.getHangmanStatus(), game.getHangmanMaxParts());

				if(game.isLost()) {
					output.println("You lose :(");
					output.println(game.getRawWord());
					s.close();
					break;
				}
				if(game.isWon()) {
					output.println("You win :)");
					output.println(game.getRawWord());
					s.close();
					break;
				}
			}
		} catch(IOException e) {
			System.out.println("You chose the wrong file:" + args[0]);
			e.printStackTrace();
		}
		
	}

}
