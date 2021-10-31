package com.mybasepackage.medium.misc;

//import java.util.*;


import java.util.HashSet;
import java.util.Set;

abstract class StringMaskImmunityRule {
    public boolean isImmuneToMasking(String string) {
        return false;
    }
}

abstract class CharacterMaskImmunityRule {
    public boolean isImmuneToMasking(String string, Integer characterIndex) {
        return false;
    };
}

class StringLengthCheckerRule extends StringMaskImmunityRule {
    public boolean isImmuneToMasking(String string) {
        return string.length() < 6;
    };
}

class EmptyStringCheckerRule extends StringMaskImmunityRule {
    public boolean isImmuneToMasking(String string) {
        return string.equals("");
    };
}

class NondigitCheckerRule extends CharacterMaskImmunityRule {
    public boolean isImmuneToMasking(String sourceString, Integer characterIndex) {
        return !Character.isDigit(sourceString.charAt(characterIndex));
    };
}

class FirstAndLastFourCharacterCheckerRule extends CharacterMaskImmunityRule {
    public boolean isImmuneToMasking(String sourceString, Integer characterIndex) {
        boolean firstCharacter = characterIndex == 0;
        boolean lastFourCharacter = characterIndex > (sourceString.length()-5);
        return firstCharacter || lastFourCharacter;
    };
}


public class Maskify {


    /**
     *      Overall logic: [0] Define rulesets for immunities.
     *                     [1] If whole string is immune for masking, early return.
     *                     [2] If not, then iterate characters and see if each character is immune to masking.
     *
     */
    public static String maskify(String creditCardNumber) {

        StringBuilder maskedCreditCardNumber = new StringBuilder();
        Character MASK_CHARACTER = '#';


        // [phase 0] construct rulesets

        Set<StringMaskImmunityRule> creditCardImmunityRuleSet = new HashSet<StringMaskImmunityRule>(){{
            add(new EmptyStringCheckerRule());
            add(new StringLengthCheckerRule());
        }};

        Set<CharacterMaskImmunityRule> characterImmunityRuleSet = new HashSet<CharacterMaskImmunityRule>(){{
            add(new NondigitCheckerRule());
            add(new FirstAndLastFourCharacterCheckerRule());
        }};


        // [phase 1] check with `StringMaskImmunityRule`s if whole string is immune to masking
        for(StringMaskImmunityRule stringRule: creditCardImmunityRuleSet) {
            if (stringRule.isImmuneToMasking(creditCardNumber)) {
                return creditCardNumber;
            }
        }

        // [phase 2] iterate characters and see if each character is immune to masking.
        for (int characterIndex=0; characterIndex<creditCardNumber.length(); characterIndex++) {
            maskCharacter: {
                for (CharacterMaskImmunityRule characterImmunityRule: characterImmunityRuleSet) {
                    if (characterImmunityRule.isImmuneToMasking(creditCardNumber, characterIndex)) {
                        // we found that an immunity can be applied.
                        // action: add original character, move on to next character.
                        maskedCreditCardNumber.append(creditCardNumber.charAt(characterIndex));
                        break maskCharacter;
                    }
                }
                maskedCreditCardNumber.append(MASK_CHARACTER);
            }
        }

        return maskedCreditCardNumber.toString();
    }


    public static void main(String[] args) {
        System.out.println(Maskify.maskify("5512103073210694"));
        System.out.println(Maskify.maskify("4556-3646-0793-5616"));
        System.out.println(Maskify.maskify("64607935616"));
    }
}


