package hangman;

import java.io.IOException;
import java.util.Set;
import java.util.HashSet;


public class Game {
	private int hangmanStatus = 0;
	private GuessWord word;
	private int hangmanMaxParts;
	private Set<Character> triedLetters;
	
	public Game(String filename, int hangmanMaxParts) throws IOException {
		this.hangmanMaxParts = hangmanMaxParts;
		this.word = new GuessWord(WordChooser.getRandomWord(filename));
		this.triedLetters = new HashSet<>();
		this.triedLetters.add('\n');
	}
	
	public void tryLetter(char letter) {
		if(triedLetters.contains(letter)) {
			if(letter != '\n') {
				System.out.println("Letter " + letter + " was already tried.");
			}
			return;
		}
		triedLetters.add(letter);
		if(!this.word.tryLetter(letter)) {
			this.hangmanStatus += 1;
		}
	}
	
	public boolean isLost() {
		return hangmanStatus >= hangmanMaxParts;
	}
	
	public boolean isWon() {
		return word.isGuessed();
	}

	public int getHangmanStatus() {
		return hangmanStatus;
	}

	public int getHangmanMaxParts() {
		return hangmanMaxParts;
	}

	public Set<Character> getTriedLetters() {
		return triedLetters;
	}

	public String getWord(char delimiter) {
		char[] wordToConvert = new char[word.length()];
		for(int i = 0; i < word.length(); ++i) {
			Character c = word.charAt(i);
			if(c != null) {
				wordToConvert[i] = word.charAt(i);
			} else {
				wordToConvert[i] = delimiter;
			}
		}
		return new String(wordToConvert);
	}

	public String getRawWord() {
		return this.word.getWord();
	}
}