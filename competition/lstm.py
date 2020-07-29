import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset
from torch.utils.data import DataLoader


class TimeSeriesDataset(Dataset):
    def __init__(self, time_series, time_step):
        self.x_dataset, self.y_dataset = self.make_sequence(time_series, time_step)
        self.x_train_set = torch.FloatTensor(self.x_dataset)
        self.y_train_set = torch.FloatTensor(self.y_dataset)

    def __len__(self):
        return len(self.x_data)

    def __getitem__(self, idx):
        x_train = self.x_train_set[idx]
        y_train = self.y_train_set[idx]
        return x_train, y_train

    def make_sequence(self, time_series, time_step):
        x_dataset, y_dataset = list(), list()

        for i in range(len(time_series)):
            end_ix = i + time_step
            if end_ix > len(time_series)-1:
                break
            
            seq_x, seq_y = time_series[i:end_ix], time_series[end_ix]
            x_dataset.append(seq_x)
            y_dataset.append(seq_y)
        return x_dataset, y_dataset


class Vanilla_LSTM(nn.Module):
    def __init__(self, hidden_size, time_step, num_layers):
        super(Vanilla_LSTM, self).__init__()
        self.lstm = nn.LSTM(1, hidden_size, num_layers, batch_first=True, bias=True)
        self.linear = nn.Linear(hidden_size, 1, bias=True)

    def forward(self, x):           # x : (batch,      seq_len, input_size)
        o, (x, c) = self.lstm(x)    # x : (num_layers, batch,   hidden_size)
        x = self.linear(x[-1])      # x : (batch,      1)
        x = x.squeeze(-1)           # x : (batch)
        return x


def train():
    time_series = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    time_step = 3

    dataset = TimeSeriesDataset(time_series=time_series, time_step=time_step)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=False)
    x_train_set = getattr(dataset, 'x_train_set')
    y_train_set = getattr(dataset, 'y_train_set')
    model = Vanilla_LSTM(hidden_size=50, time_step=time_step, num_layers=1)
    criterion = nn.MSELoss(reduction='mean')
    optimizer = optim.Adam(model.parameters(), lr=1e-2, weight_decay=1e-5)

    print(f'* time_series : {time_series}')
    for x_train in x_train_set:
        print(f'{x_train} > next?')
    
    epochs = 3000
    for epoch in range(epochs + 1):
        hypothesis = model(x_train_set.unsqueeze(-1))
        cost = criterion(hypothesis, y_train_set)

        optimizer.zero_grad()
        cost.backward()
        optimizer.step()

        print(f'Epoch [{epoch:4d}/{epochs}], Cost: {cost.item():.6f}, Forecast:{hypothesis.data}', end='\r')
    #print(f'{hypothesis.data}')
    
def main():
    train()

if __name__ == "__main__":
    main()
