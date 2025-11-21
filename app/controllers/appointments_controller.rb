class AppointmentsController < ApplicationController
  def index
    @appointments = Appointment.where(patient: current_user)
  end

  def new
    @appointment = Appointment.new
  end

  def create
    @appointment = Appointment.new(appointment_params)
    @appointment.patient = current_user
    @appointment.status = :pending

    if @appointment.save
      redirect_to appointments_path, notice: 'Appointment was successfully created.'
    else
      render :new
    end
  end

  def destroy
    @appointment = Appointment.find(params[:id])
    @appointment.update(status: :cancelled)
    redirect_to appointments_path, notice: 'Appointment was successfully cancelled.'
  end

  private

  def appointment_params
    params.require(:appointment).permit(:doctor_id, :scheduled_at, :note)
  end

  def current_user
    # Placeholder for authentication logic
    User.first
  end
end
