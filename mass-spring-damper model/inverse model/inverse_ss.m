
clc
clear

%% system parames
dt = 1e-3; % simulation time step 
m1 = 7 * 1e-3; % finger mass
m2 = 34.05 * 1e-3; % key mass
% m1 = 70 * 1e-2; % finger mass
% m2 = 34.05 * 1e-2; % key mass
% c0 = 10.5;
% c1 = 10.5;
% c2 = 10.5;
c = 0.5;
c0 = c;
c1 = c;
c2 = 0.3;
k2 =0.3012 * 1000; % key stiffness, N/m

%% UR5 Control params
depth = -30 * 1e-3; % m
% depth = -7 * 1e-3; % m
% vel = 100 * 1e-3;   % m/s
% acc = 1; %m/s^2 
% holdtime = 0.5;
holdtime = 0.5;

% figure
pressure_list = [0,20,40,60,80];
% pressure_list = [0,20,40];
% pressure_list = [30,50,70];
% pressure_list = [0,40,80];
% pressure_list = [20];
% vel_list = linspace(0.01,0.08,15);
vel_list = linspace(0.01,0.08,15);
% vel_list = [0.05,0.055,0.06,0.065,0.07,0.075,0.08];
% vel_list = [0.05];
midi_all = [];
hold_time_all = [];
midi_down_poz_list = [];
i = 1
% figure
for pressure = pressure_list
    kf = 1.19*pressure+75.41;  
    k1 = kf; % finger stiffness
    k0 =kf; % finger stiffness 
%     k2 = k2*0.065;
    k2 = k2*0.20;
    midi_l = [];
    hold_time_l = [];
    for vel = vel_list
        
        %% Do simulation
        t_stop = 2*-depth/vel+holdtime;
        disp(t_stop);
        res=sim('StateSpacev2','StartTime','0','StopTime',num2str(t_stop),'FixedStep',num2str(dt));
        
        time = res.tout;
        x0 = res.input.data;
        x1 = res.output.data(:,1);
        x2 = res.output.data(:,2);
        v0 = diff(x0)/dt;
        v1 = diff(x1)/dt;
        v2 = diff(x2)/dt;

        [min_x2,index_mx2] = min(x2);
        thres = -0.005;
%         thres = min_x2/5;
%         thres = -0.001;
% %         thres = -1 * 1e-3;
        x2_half =  x2(1:round((size(x2,1)/2)));
        [ d, midi_down_poz] = min( abs( x2_half- thres) );
        midi_down_poz_list = [midi_down_poz_list,midi_down_poz];
        midi = -1*v2(midi_down_poz(1));
        midi_l = [midi_l,midi];
        hold_time_l = [hold_time_l,sum(x2(:)<thres)*dt];

                
        %% draw displacement of x0 x1 x2
%         figure
%         plot(time, x0,'y', 'linewidth',2)
%         hold on
%         plot(time, x1,'r', 'linewidth',2)
%         hold on
%         plot(time, x2,'b', 'linewidth',2)
%         
% 
%         
%         figure
%         plot( v0,'y', 'linewidth',2)
%         hold on
%         plot( v1,'r', 'linewidth',2)
%         hold on

%         plot( v2,'b', 'linewidth',2)
%         hold on
%         plot(midi_down_poz(1),-midi,'red')
%         hold on
        
%         fname = sprintf('model_output_p%dv%d.mat', pressure,vel);
%         save(fname,'time','x0','x1','x2','v0','v1','v2');
    end

    midi_all=[midi_all,midi_l];
    hold_time_all = [hold_time_all,hold_time_l];
end
midi_all = reshape(midi_all,[],1);
hold_time_all = reshape(hold_time_all,[],1);
save('model_midi_new_real_thres_0.001_correct_param_024_new50.mat','midi_all','hold_time_all');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% %% draw FR response
% A = [0 1 0 0; 
%     -(k0+k1)/m1 -(c0+c1)/m1 k1/m1 c1/m1;
%     0 0 0 1; 
%     k1/m2 c1/m2 -1*(k1+k2)/m2 -1*(c1+c2)/m2];
% 
% B = [c0/m1;
%     k0/m1-(c0^2+c0*c1)/m1^2;
%     0;
%     c0*c1/(m1*m2)];
% 
% C = [1 0 0 0;
%     0 0 1 0];
% 
% D = [0;
%     0];
% 
% sys1 = ss(A,B,C,D);
% % sys1 = ss(A1,B1,C1,D1,'TimeUnit','seconds','InputUnit','seconds');
% omeg = logspace(-1,5); 
% sysg = frd(sys1,omeg); 
% bode(sysg,'r-');
