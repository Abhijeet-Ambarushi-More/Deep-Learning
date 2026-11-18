# ht = tanh(Wx * Xt + Wh * ht -1 + b)

# Xt    : Current input
# Wx    : Weight of current input
# ht-1  : previous hidden state
# Wh    : Weight of previous hidden state
# b     : bias
# tanh  : Activation function(-1 to 1)
# ht    : New hidden state

import numpy as np
def sigmoid(X):
    return 1 / (1 + np.exp(-X))

def MarvellousRNNPredictions():
    print("Calculations of RNN")

    # food was not good
    inputs = [1, 2, 5, 3]

    hidden_state = 0

    # RNN parameters
    Wx = 0.5
    Wh = 0.8
    bias = 0.1

    # Step 1 : RNN calculations
    for time_step , X in enumerate(inputs):
        previous_hidden_state = hidden_state

        weighted_input = Wx * X
        weighted_memory = Wh * previous_hidden_state

        total = weighted_input + weighted_memory + bias

        hidden_state = np.tanh(total)

        print("Time step : ",time_step+1)
        print("Input : ",X)
        print("Hidden state : ",hidden_state)
        print("-"*60)

    # Step 2 : Final hidden state
    print("Final Hidden State : ",hidden_state)

    # Step 3 : Output layer
    # Output = Wy * FinalHiddenState + Output Bias

    Wy = 1.0
    output_bias = 0.0

    output = (Wy * hidden_state + output_bias)

    print("Raw output : ", output)

    # Step 4 : Apply the sigmoid
    probabilty = sigmoid(output)

    print("Probabilty is : ",probabilty)

def main():
    MarvellousRNNPredictions()

if __name__ == "__main__":
    main()