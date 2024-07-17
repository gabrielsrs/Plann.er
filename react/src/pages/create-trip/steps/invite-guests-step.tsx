import { ArrowRight, UserRoundPlus } from "lucide-react";
import { Button } from "../../../components/button";

interface InviteGuestsStepProps {
    openGuestModal: () => void
    emailsToInvite: string[]
    openConfirmTripModal: () => void
}

export function InviteGuestsStep ({
    openGuestModal,
    emailsToInvite,
    openConfirmTripModal,
}: InviteGuestsStepProps) {
    return (
        <div className="h-16 bg-zinc-900 px-4 rounded-xl flex items-center shadow-shape gap-3">
            <button type="button" onClick={openGuestModal} className="flex items-center gap-2 flex-1">
                <UserRoundPlus className="size-5 text-zinc-400"/>
                {emailsToInvite.length > 0 ? (
                    <span className="text-lg placeholder-zinc-400 flex-1 text-left">{emailsToInvite.length} pessoa(s) convidada(s)</span>
                ): (
                    <span className="text-lg placeholder-zinc-400 flex-1 text-left">Quem estará na viagem?</span>
                )}
            </button>
            
            <Button variant={"primary"} onClick={openConfirmTripModal}>
                Confirmar Viagem
                <ArrowRight className="size-5"/>
            </Button>
        </div>
    )
}