
plot3(data(:,1),data(:,2),data(:,3),".")
% hold on
% plot3(XTest(:,1),XTest(:,2),YTest,'*')
% hold off
xlabel("vacuum pressure")
ylabel("UR5 velocity")
zlabel("on Vel")

% legend('predicted value','ground truth')