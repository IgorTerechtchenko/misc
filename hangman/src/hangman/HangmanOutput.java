package hangman;

import java.io.PrintStream;
import java.util.Set;

public class HangmanOutput {
	private PrintStream stream;
	
	public HangmanOutput(PrintStream stream) {
		this.stream = stream;
	}
	
	public void println(String string) {
		this.stream.println(string);
	}

	public void println(int currentState, int maxParts) {
		this.stream.println(currentState + "\\" + maxParts);
	}

	public void println(Set<Character> triedLetters) {
		this.stream.println("Tried letters:");
		for(Character c : triedLetters) {
			if(c.charValue() != '\n') {
				this.stream.print(c + " ");
			}
		}
		this.stream.println();
	}
}
