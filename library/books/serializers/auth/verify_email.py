from rest_framework import serializers
from books.models.auth.email_verification import VerificationCode

class VerifyEmailSerializer(serializers.Serializer):
    verification_code = serializers.CharField(min_length=6, max_length=6)

    def validate_verification_code(self, value):
        # We only accept codes that contain numbers
        if not value.isdigit():
            raise serializers.ValidationError(
                "Verification code must be numeric."
            )
        
        # Let"s check if the code is valid or if it has already been validated
        if not self.is_valid_verification_code(value):
            raise serializers.ValidationError(
                "Invalid or already verified verification code!"
            )
        
        # We ensure that the code is deactivated after the verification process
        self.mark_code_as_verified(value)
        
        return value

    def is_valid_verification_code(self, verification_code):
        try:
            verification_record = VerificationCode.objects.get(
                verification_code=verification_code
            )
            if verification_record.is_verified:
                return False  
            return True
        except VerificationCode.DoesNotExist:
            return False  

    def mark_code_as_verified(self, verification_code):
        try:
            verification_record = VerificationCode.objects.get(
                verification_code=verification_code
            )
            verification_record.is_verified = True 
            verification_record.save()
        except VerificationCode.DoesNotExist:
            raise serializers.ValidationError("Invalid verification code!")
