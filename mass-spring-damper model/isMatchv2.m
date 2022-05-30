clc

a = [5.85
5.86
5.81
5.74
5.7
5.47
5.29
5.05
4.34];
a = flip(a);

b = [5.22
5.29
5.17
5.11
4.94
4.8
4.59
4.37
3.31];
b = flip(b);

ratio = a./b;

ratio_ref = [1.2386 1.2020 1.1970 1.1599 1.1451 1.1190 1.1192 1.1093 1.1041];

hwR = (ratio - ratio_ref)/ratio_ref
hwR = 100*abs(hwR(2:end))
figure 
plot(hwR,'--k*','linewidth',2,'markersize',10)
axis([0 10 0 10])

% 
% figure
% % plot(a,'--r*','linewidth',2,'markersize',10)
% % hold on
% % plot(b,'--b*','linewidth',2,'markersize',10)
% % grid on
% plot(ratio_ref,'--r*','linewidth',2,'markersize',10)
% hold on
% plot(ratio,'--b*','linewidth',2,'markersize',10)
% grid on
