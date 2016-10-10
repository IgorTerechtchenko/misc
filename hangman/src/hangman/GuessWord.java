package hangman;

public class GuessWord {
	
	private String word;
	private boolean[] letterStatus;
	
	public GuessWord(String word) {
		this.word = word;
		this.letterStatus = new boolean[word.length()];
		for(int i = 0; i < word.length(); ++i) {
			letterStatus[i] = false;
		}
	}
	
	public boolean tryLetter(char letter) {
		boolean letterMet = false;
		for(int i = 0; i < word.length(); ++i) {
			if(word.charAt(i) == letter) {
				letterStatus[i] = true;
				letterMet = true;
			}
		}
		return letterMet;
	}
	
	public boolean isGuessed() {
		for(boolean letter : letterStatus) {
			if(letter == false) {
				return false;
			}
		}
		return true;
	}
	
	public Character charAt(int position) {
		if(position > word.length()) {
			throw new ArrayIndexOutOfBoundsException("Position is too large.");
		}
		
		if(letterStatus[position]) {
			return word.charAt(position);
		}
		return null;
	}
	
	public int length() {
		return word.length();
	}

	public String getWord() {
		return word;
	}
}
